import React from "react";
import { Link, useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();
  const isAuthenticated = !!localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-white text-xl font-bold">
          Dashboard
        </Link>
        <div>
          {isAuthenticated ? (
            <button
              onClick={handleLogout}
              className="text-gray-300 hover:text-white mx-2"
            >
              Logout
            </button>
          ) : (
            <Link to="/login" className="text-gray-300 hover:text-white mx-2">
              Login
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
