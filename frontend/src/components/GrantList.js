
import React, { useState, useEffect } from 'react';

const API_URL = "https://grant-matching-app.onrender.com";

function GrantList() {
    const [grants, setGrants] = useState([]);

    useEffect(() => {
        fetch(API_URL + "/grants/")
            .then(res => res.json())
            .then(data => setGrants(data));
    }, []);

    return (
        <div>
            <h2>Grants</h2>
            <ul>
                {grants.map(g => (
                    <li key={g.id}>{g.title} - {g.technology}</li>
                ))}
            </ul>
        </div>
    );
}

export default GrantList;
