 
 import "../kategory/category.css"
import {Link} from "react-router-dom"

export function Catigory() {
    return <>
    <div className="container">
        <div className="category">
        <h3 className="category__username">User Name</h3>
            <ul className="category__list">
                <li className="category__item"> 
                <Link className="category__IT" to={"/IT"}></Link>
                </li>
                <li className="category__item">
                <Link className="category__IQ" to={"/IQ"}></Link>
                </li>
                <li className="category__item"></li>
                <li className="category__item"></li>
                <li className="category__item"></li>
                <li className="category__item"></li>
                <li className="category__item"></li>
                <li className="category__item"></li>
                <li className="category__item"></li>
            </ul>
            
        </div>
    </div>
    </>
}
