import './App.css';
import { useState, useEffect } from 'react'
import { Routes, Route } from 'react-router-dom'
import { RequireAuth } from 'react-auth-kit'
import { Login } from './pages/login'
import { Dashboard } from './pages/dashboard';

function App() {
  const [user, setUser] = useState('')

  useEffect(() => {
    setUser(user)
  }, [user])

  return (
    <div className="App">
      <header className="App-header">
        <Routes>
          <Route path='/' element={<Login setUser={setUser} />} />
          <Route path='/dashboard' element={
          // <RequireAuth loginPath='/'>
            <Dashboard user={user}></Dashboard>
          // </RequireAuth>} 
          }/>
        </Routes>
      </header>
    </div>
  );
}

export default App;
