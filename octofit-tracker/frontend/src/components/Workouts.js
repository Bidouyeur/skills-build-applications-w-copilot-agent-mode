import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://potential-carnival-j7q6q94px7jfp95g.github.dev-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Erreur lors de la récupération des entraînements :', error));
  }, []);

  return (
    <div className="card shadow p-4 mb-4 bg-white rounded">
      <h1 className="mb-4 text-primary">Entraînements</h1>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-primary">
            <tr>
              <th>Nom</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map(workout => (
              <tr key={workout._id}>
                <td>{workout.name}</td>
                <td>{workout.description}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button className="btn btn-primary mt-3">Ajouter un entraînement</button>
    </div>
  );
}

export default Workouts;
