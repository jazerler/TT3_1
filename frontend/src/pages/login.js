import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useSignIn } from "react-auth-kit";
import 'bootstrap/dist/css/bootstrap.css'

function Login(props) {
    const [errorText, setError] = useState("");
    const [user, setUser] = useState("");
    const [password, setPassword] = useState("");

    const signIn = useSignIn();
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError("");
    
        try {
          const response = await fetch(
            "http://localhost:5000/login", // to change to backend API
            {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify() // userid and password to send to backend
            }
          );
    
          if (response.status !== 200) {
            throw "Email or password mismatch"
          }
    
          signIn({
            token: response.headers.get('Authorization'),
            expiresIn: 3600,
            tokenType: "Bearer",
            authState: { user: user },
          });
    
          navigate('/dashboard')
        } catch (err) {
          setError(err);
        }
    };

    return (
        <div className="App Background">
            <header>
              <h1>Expense claims</h1>
            </header>
            <form onSumbit={handleSubmit}>
              <div className="input-group">
                <label htmlFor="username">Username: </label>
                <input type="text" id="username" value={user}
                onChange={e => setUser(e.target.value)} />
              </div>
              <div className="input-group">
                <label htmlFor="password">Password: </label>
                <input type="password" id="password" value={password}
                onChange={e => setPassword(e.target.value)} />
              </div>
              <div button
                type="button"
                className="btn btn-danger btn-lg"
                style={{ height: 50, width: 325 }}
              >
                Login
              </div>
              <div button
                type="button"
                className="btn btn-outline-danger btn-lg"
                style={{ height: 50, width: 325 }}
              >
                Get Started
              </div>
            </form>
          </div>
    )
}



export { Login };