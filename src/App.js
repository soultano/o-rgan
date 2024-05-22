
import { Route, Routes } from "react-router-dom";
import "./App.css";

import {Register} from "./components/Register/Register.js"
import { Catigory } from "./components/kategory/category";

function App() { 
  return (
   <>
   <Routes>
<Route path="/" element={<Register/>}>
 </Route>
</Routes>
    
    <Routes>
<Route path="/Catigory" element={<Catigory />}>
 </Route>
</Routes>
   </>
  );
}

export default App;
