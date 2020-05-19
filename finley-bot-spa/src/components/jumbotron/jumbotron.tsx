import React, { Component } from 'react';
import './jumbotron.css';
import socials from '../../images/socials.png';

import DiscordBox from '../discord-box';

const Jumbotron: React.FC = () => {
    return (
        <div className="jumbotron">
            <h2>Discord Bot</h2>
            <p className="text-secondary"> Express yourself </p>
            <p className="text-secondary">Integrate video and audio files via Youtube</p>
            <p className="text-secondary">Moderate users actions.</p>
            <p className="text-warning">Лучше шалава дочь чем жить на коленях</p>
            <p className="text-info">Папкин бродяка мамин бродяка</p>
            <div className="social-box">
                <a href= "https://discord.com/oauth2/authorize?client_id=700379451246116894&scope=bot&permissions=8">
                    <button type="button" className="btn btn-warning btn-lg">
                        Open Discord
                    </button>    
                </a>
                <div className="right-wrap">
                    <img className="social-image" src={socials} alt="socials"></img>
                    <div className="icons-wrap">
                    {/* <div className="fb-like" data-href="https://www.facebook.com/WashingtonStateLibrary" data-width="" data-layout="button" data-action="like" data-size="large" data-share="true"></div> */}
                        <a href="https://developers.facebook.com/docs/facebook-login">
                            <i className="fa fa-facebook-official" aria-hidden="true"></i>
                        </a>
                        <a href="https://www.instagram.com/developer">
                            <i className="fa fa-instagram"></i>
                        </a>
                        <a href="https://developers.google.com/identity/">
                            <i className="fa fa-google" aria-hidden="true"></i>
                        </a>
                    </div>
                    
                </div>
            </div>
        </div>
    );
}

export default Jumbotron;
