import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useSignIn } from "react-auth-kit";
import 'bootstrap/dist/css/bootstrap.css'

function Login(props) {
    const [error, setError] = useState("");
    const signIn = useSignIn();
    const navigate = useNavigate();

    const onSubmit = async (values) => {
        setError("");
    
        try {
          const response = await fetch(
            "http://localhost:5000/login", // to change to backend
            {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(values)
            }
          );
    
          if (response.status !== 200) {
            throw "Email or password mismatch"
          }
    
          signIn({
            token: response.headers.get('Authorization'),
            expiresIn: 3600,
            tokenType: "Bearer",
            authState: { userid: values.userid },
          });
    
          props.setUser('') // set input user id
          navigate('/')
        } catch (err) {
          setError(err);
        }
    };

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