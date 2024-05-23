import React from 'react';
import { NavLink } from "react-router-dom";
import "../Register/Register.css";

export function Register() {
    return (
        <>
            <div className="container">
                <div className="register">
                    <div>
                        <h2 className="text_register">Welcome</h2>
                        <p className="description_register">
                            Vazifalarni bajarib ball to'plang va ularni mukofotlarga almashtiring.
                        </p>
                    </div>
                    <div className="button_box">
                        {/* Start tugmasi */}
                        <NavLink className="button_start" to={'/Category'}></NavLink>
                        <span className="Start_text">Start</span>
                    </div>
                </div>
            </div>
        </>
    );
}
