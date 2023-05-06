import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useSignIn } from "react-auth-kit";

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
        <a>hello</a>
    )
}

export { Login };