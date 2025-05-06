import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://potential-carnival-j7q6q94px7jfp95g.github.dev-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Erreur lors de la récupération des activités :', error));
  }, []);

  return (
    <div className="card shadow p-4 mb-4 bg-white rounded">
      <h1 className="mb-4 text-primary">Activités</h1>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-primary">
            <tr>
              <th>Utilisateur</th>
              <th>Type d'activité</th>
              <th>Durée</th>
            </tr>
          </thead>
          <tbody>
            {activities.map(activity => (
              <tr key={activity._id}>
                <td>{activity.user}</td>
                <td>{activity.activity_type}</td>
                <td>{activity.duration}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button className="btn btn-primary mt-3">Ajouter une activité</button>
    </div>
  );
}

export default Activities;
