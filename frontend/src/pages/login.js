import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useSignIn } from "react-auth-kit";
import 'bootstrap/dist/css/bootstrap.css'

function Login(props) {
    const [errorText, setError] = useState('');
    const [user, setUser] = useState("");
    const [password, setPassword] = useState("");

    const signIn = useSignIn();
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError("");

        let formData = new FormData();
        formData.append('EmployeeID', user)
        formData.append('Password', password)
    
        try {
          const response = await fetch(
            "http://127.0.0.1:5000/login",
            {
              method: 'POST',
              headers: {
                'content-type': 'multipart/form-data'
              },
              body: formData
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
          // get access token
        } catch (err) {
          setError("Backend not setup");
        }
    };

    return (
        <div className="App Background">
            <div className='login-modal'>
                <image path='../images/dbs_login.png'></image>
                <br />
                <form>
                <div className="input-group">
                    <label htmlFor="username">Username: </label>
                    <input type="text" id="username" value={user}
                    onChange={e => setUser(e.target.value)} />
                </div>
                <br />
                <div className="input-group">
                    <label htmlFor="password">Password: </label>
                    <input type="password" id="password" value={password}
                    onChange={e => setPassword(e.target.value)} />
                </div>
                <br />
                <div button
                    type="login"
                    className="btn btn-danger btn-lg"
                    style={{ height: 50, width: 325 }}
                    onClick={handleSubmit}
                >
                    Login
                </div>
                <br /><br />
                <div button
                    type="button"
                    className="btn btn-outline-danger btn-lg"
                    style={{ height: 50, width: 325 }}
                >
                    Get Started
                </div>
                <div>
                    {errorText}
                </div>  
                </form>
            </div>
          </div>
    )
}



export { Login };