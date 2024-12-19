import { useState, useEffect } from 'react';
import ImageGenerator from './components/ImageGenerator';
import NavBar from './components/NavBar';
import Login from './components/Login';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <div className="min-h-screen bg-gray-50">
      {isLoggedIn ? (
        <>
          <NavBar />
          <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
            <div className="px-4 py-6 sm:px-0">
              <ImageGenerator />
            </div>
          </main>
        </>
      ) : (
        <div className="min-h-screen flex items-center justify-center">
          <Login onLoginSuccess={() => setIsLoggedIn(true)} />
        </div>
      )}
    </div>
  );
}

export default App;