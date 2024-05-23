from django.core.management.base import BaseCommand
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ContextTypes, filters
)
from questions.models import Question
from users.models import CustomUser
from questions.serializers import QuestionSerializer
from asgiref.sync import sync_to_async

class Command(BaseCommand):
    help = 'Start the Telegram bot'

    def handle(self, *args, **kwargs):
        TELEGRAM_BOT_TOKEN = '7160702999:AAFSG-dK9f_0Mt5JGeGxMOOkaSISHC-bV60'

        application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

        # Add command and message handlers
        application.add_handler(CommandHandler('start', self.start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

        # Start the bot
        application.run_polling()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.message.from_user

        # Check if the user has a username
        if user.username:
            identifier = user.username
        else:
            # Use the first name as an identifier if no username is provided
            identifier = user.first_name

        # Register or get user (wrapped in sync_to_async)
        custom_user, created = await sync_to_async(CustomUser.objects.get_or_create)(username=identifier)
        await sync_to_async(custom_user.save)()

        # Prepare the web app button
        web_app_url = 'https://t.me/programming_learner'
        keyboard = [
            [InlineKeyboardButton("Continue the quiz", web_app={"url": web_app_url})]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send welcome message with the web app button
        await update.message.reply_text(
            f'Hello, {user.first_name}! Welcome to the Quiz Bot. Click the button below to continue the quiz.',
            reply_markup=reply_markup
        )

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.message.from_user
        username = user.username

        # Get the custom user (wrapped in sync_to_async)
        custom_user = await sync_to_async(CustomUser.objects.get)(username=username)

        # Fetch a random question (wrapped in sync_to_async)
        question = await sync_to_async(lambda: Question.objects.order_by('?').first())()
        question_data = QuestionSerializer(question).data

        # Prepare the reply markup
        reply_markup = ReplyKeyboardMarkup(
            [[question_data['option_a'], question_data['option_b']]],
            one_time_keyboard=True
        )

        # Save current question to context
        context.user_data['current_question'] = question.id

        # Send the question
        await update.message.reply_text(
            question_data['question_text'],
            reply_markup=reply_markup
        )

        # Add handler for the answer
        context.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_answer))

    async def handle_answer(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.message.from_user
        username = user.username

        # Get the custom user (wrapped in sync_to_async)
        custom_user = await sync_to_async(CustomUser.objects.get)(username=username)
        selected_option = update.message.text

        # Retrieve the current question (wrapped in sync_to_async)
        question_id = context.user_data.get('current_question')
        question = await sync_to_async(Question.objects.get)(id=question_id)

        # Check the answer and update the score
        if selected_option == question.answer:
            custom_user.ball += 1
            await update.message.reply_text('Correct! Your score has been updated.')
        else:
            await update.message.reply_text('Incorrect. Better luck next time!')

        await sync_to_async(custom_user.save)()

        # Remove the answer handler to avoid duplication
        context.application.remove_handler(self.handle_answer, update.message.chat_id)

        # Prompt for the next question
        await self.handle_message(update, context)
