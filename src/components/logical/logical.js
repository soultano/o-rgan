import React, { useState, useRef } from "react";
import "../logical/logical.css";
import data from '../../assets/fileJson/data.json'; // JSON faylni import qilish
export default function Logicals() {
    // Holatlarni e'lon qilish
    const [currentIndex, setCurrentIndex] = useState(0); // Hozirgi savolning indeksini saqlaydi
    const [paxtaCount, setPaxtaCount] = useState(0); // To'g'ri javoblar uchun berilgan "PAXTA" sonini saqlaydi

    // Tugmalar uchun referenslar
    let ref_a = useRef();
    let ref_b = useRef();

    // Javobni tekshiruvchi funksiya
    const handleAnswer = (answer) => {
        // Agar foydalanuvchi tanlagan javob to'g'ri bo'lsa, "PAXTA" sonini oshiramiz
        if (answer === data[currentIndex].answer) {
            setPaxtaCount(paxtaCount + 1);
        }
        // Keyingi savolga o'tamiz, oxiriga yetganda boshidan boshlaymiz
        setCurrentIndex((prevIndex) => (prevIndex + 1) % data.length);
    };
    return (
        <> 
            <div className="container">
                <div className="logical">
                    <h3 className="category__username">User Name</h3>
                    <div className="logical__display">
                        <p className="logical__text">{data[currentIndex].question_text}</p>
                    </div>
                    <div className="logical__variants">
                        <p className="logical__variant-a oneStillSpan">{data[currentIndex].option_a}</p> 
                        <p className="logical__variant-b oneStillSpan">{data[currentIndex].option_b}</p> 
                    </div>
                    <div className="logical__box">
                        <span className="ball">{paxtaCount}</span> 
                        <span className="ball ball__text">PAXTA</span>
                    </div>
                    <div className="logical__buttons">
                        <button 
                            ref={ref_a} 
                            className="logical__buttons-a oneStill" 
                            onClick={() => handleAnswer('A')}>
                          
                        </button>
                        <button 
                            ref={ref_b} 
                            className="logical__buttons-b oneStill" 
                            onClick={() => handleAnswer('B')}>
                         
                        </button>
                    </div>
                </div>
                <div className="PainPort">
                    <ul className="category__list PainPort__list">
                        <li className="PainPort__item">
                            <span variant="text">Squard</span>
                        </li>
                        <li className="PainPort__item"> 
                            <span variant="text">Refresh</span>
                        </li>
                        <li className="PainPort__item"> 
                            <span variant="text">Profile</span>
                        </li>
                    </ul>
                </div>
            </div>
        </>
    )
}
