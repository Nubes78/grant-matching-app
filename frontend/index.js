  
import React, { useState, useEffect } from 'react';

const API_URL = "https://grant-matching-app.onrender.com"; // Update this to your deployed backend

function App() {
    const [grants, setGrants] = useState([]);
    const [businesses, setBusinesses] = useState([]);
    
    useEffect(() => {
        fetch(API_URL + "/grants/")
            .then(res => res.json())
            .then(data => setGrants(data));
        fetch(API_URL + "/businesses/")
            .then(res => res.json())
            .then(data => setBusinesses(data));
    }, []);

    return (
        <div>
            <h1>Grant Matching App</h1>
            <h2>Grants</h2>
            <ul>
                {grants.map(g => (
                    <li key={g.id}>{g.title} - {g.technology}</li>
                ))}
            </ul>
            <h2>Businesses</h2>
            <ul>
                {businesses.map(b => (
                    <li key={b.id}>{b.name} - {b.industry}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
