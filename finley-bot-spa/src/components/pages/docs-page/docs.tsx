import React, { Component } from 'react';
import './docs.css';

const Docs: React.FC  = () => {

    return (
        <div className="docs">
            <h3>Documentation</h3>
            <h6 className="text-muted">On this page you cand find a full list of commands which you can easily utilize in discord via our bot</h6>
            <table className="table table-hover">
            <thead>
                <tr className="table-info">
                    <th scope="row">#</th>
                    <td>Command</td>
                    <td>Type</td>
                    <td>Description</td>
                </tr> 
            </thead>
            <tbody>
                <tr className="table-active">
                    <th scope="row">1</th>
                    <td>roll</td>
                    <td>Column content</td>
                    <td>Column content</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>game_rps</td>
                    <td>Column content</td>
                    <td>Column content</td>
                </tr>
                <tr className="table-active">
                    <th scope="row">3</th>
                    <td>unban</td>
                    <td>Column content</td>
                    <td>Column content</td>
                </tr>
                <tr>
                    <th scope="row">4</th>
                    <td>level `username`</td>
                    <td>Column content</td>
                    <td>Column content</td>
                </tr>
                    
                <tr className="table-active">
                    <th scope="row">5</th>
                    <td>card</td>
                    <td>Column content</td>
                    <td>Column content</td>
                </tr>
                <tr>
                    <th scope="row">6</th>
                    <td>Column content</td>
                    <td>Column content</td>
                    <td>Column content</td>
                </tr>
            </tbody>
            </table> 
        </div>
    );
}

export default Docs;
