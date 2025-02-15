
import React, { useState, useEffect } from 'react';

const API_URL = "https://grant-matching-app.onrender.com";

function BusinessList() {
    const [businesses, setBusinesses] = useState([]);

    useEffect(() => {
        fetch(API_URL + "/businesses/")
            .then(res => res.json())
            .then(data => setBusinesses(data));
    }, []);

    return (
        <div>
            <h2>Businesses</h2>
            <ul>
                {businesses.map(b => (
                    <li key={b.id}>{b.name} - {b.industry}</li>
                ))}
            </ul>
        </div>
    );
}

export default BusinessList;
