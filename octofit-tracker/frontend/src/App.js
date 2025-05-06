
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import './App.css';
// Utilisation du logo depuis le dossier public

function App() {
  return (
    <Router>
      <div className="container-fluid p-0 min-vh-100 bg-light">
        <nav className="navbar navbar-expand-lg navbar-dark shadow">
          <div className="container-fluid">
            <Link className="navbar-brand fw-bold d-flex align-items-center" to="/">
              <img src={process.env.PUBLIC_URL + '/octofitapp-small.png'} alt="OctoFit Logo" className="octofit-logo" />
              OctoFit Tracker
            </Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activités</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Équipes</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Utilisateurs</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Entraînements</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        <div className="container py-4">
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/" element={
              <div className="d-flex flex-column align-items-center justify-content-center" style={{ minHeight: '60vh' }}>
                <div className="card shadow-lg p-4 mb-4 bg-white rounded" style={{ maxWidth: 600 }}>
                  <h1 className="display-4 text-primary mb-3 text-center">Bienvenue sur OctoFit Tracker</h1>
                  <p className="lead text-center">L'application de suivi fitness pour Mergington High School. Utilisez le menu pour naviguer entre les activités, équipes, utilisateurs, leaderboard et entraînements.</p>
                </div>
              </div>
            } />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
