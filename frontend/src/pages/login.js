import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login(props) {
    return (
        <div className="App Background">
            <header>
              <h1>Expense claims</h1>
            </header>
            <form>
              <div className="input-group">
                <label htmlFor="username">Username: </label>
                <input type="text" id="username" />
              </div>
              <div className="input-group">
                <label htmlFor="password">Password: </label>
                <input type="password" id="password" />
              </div>
              <button type="login" className="submit-btn">
                Log in
              </button>
            </form>
          </div>
    )
}



export { Login };