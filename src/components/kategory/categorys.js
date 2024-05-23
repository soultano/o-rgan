import React from "react";
import { Link } from "react-router-dom";
import "../kategory/category.css";

export default function Category() {
    return (
        <div className="container">
            <div className="category">
                <h3 className="category__username">User Name</h3>

                {/* Kategoriyalar ro'yxati */}
                <ul className="category__list">
                    <li className="category__item">
                        <Link className="category__IT" to={"/IT"}></Link>
                    </li>
                    <li className="category__item">
                        <Link className="category__IQ" to={"/IQ"}></Link>
                    </li>
                    {/* Boshqa kategoriyalar uchun qatorlar */}
                    <li className="category__item"></li>
                    <li className="category__item"></li>
                    <li className="category__item"></li>
                    <li className="category__item"></li>
                    <li className="category__item"></li>
                    <li className="category__item"></li>
                    <li className="category__item"></li>
                </ul>

                {/* Yo'nalishlar paneli */}
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
        </div>
    );
}
