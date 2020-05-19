import React, { Component } from 'react';
import './about.css';

import DiscordBox from '../../discord-box';
import TeamService from '../../../services/team-service';

interface TeamProps {
    members: object[]
}

const About: React.FC <TeamProps> = () => {

    const team = new TeamService();
    const data = team.getData();

    return (
        <div className="about">
            {
                data.map((person) => {
                    return <DiscordBox 
                    member={person}
                    />
                })    
            }
        </div>
    );
}

export default About;
