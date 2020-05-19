import React, { Component } from 'react';
import './discord-box.css';

interface DiscordBoxProps {
    member: {
        id: number,
        name: string,
        age: number,
        position: string, 
        description: string,
        imageUrl: any,
    }
}

const DiscordBox: React.FC <DiscordBoxProps> = ({member}) => {

    const { id, name, position, age, description, imageUrl } = member;

    return (
        <div className="box container card border-warning mb-3">
            <div className="img-wrap">
                <img src={imageUrl} alt="member"></img>
            </div>
            <div className="card-header">
                <h4 className="card-title">
                    {name}
                </h4>
                <h6>
                    {position}
                </h6>
            </div>
            <div className="card-body">
                <p className="card-text">
                    {description}
                </p>
                <a href= "https://discord.com/oauth2/authorize?client_id=700379451246116894&scope=bot&permissions=8">
                    <button type="button" className="btn btn-info btn-lg">
                        Open Instagram
                    </button>    
                </a>
            </div>
        </div>
    );
}

export default DiscordBox;
