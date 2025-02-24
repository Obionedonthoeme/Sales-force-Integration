import React, { useState } from 'react';
import axios from 'axios';

function TicketForm() {
    const [subject, setSubject] = useState("");
    const [description, setDescription] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/tickets/', { subject, description });
            alert(`Ticket Created: ${response.data.ticket_id}`);
        } catch (err) {
            alert('Failed to create ticket');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Subject" value={subject} onChange={(e) => setSubject(e.target.value)} required />
            <textarea placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} required />
            <button type="submit">Submit Ticket</button>
        </form>
    );
}

export default TicketForm;

