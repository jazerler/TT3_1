import Claims from '../components/Claims.js';

function Dashboard(props) {
    return (
        <div>
            <header>
                <h1>Welcome, Username</h1>
                <h2>Your claim records:</h2>
            </header>
            
            <Claims />


        </div>
        
    )
}

export { Dashboard };