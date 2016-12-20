import React from "react";
import ReactDOM from "react-dom";
import Bootstrap from 'bootstrap/dist/css/bootstrap.css';
var App = React.createClass({
    render: function () {
        return (
            <div>
                <h1>
                    Hello, Photogram!
                </h1>
                <a href="https://github.com/KirovVerst/photogram">GitHub Repository</a>
            </div>
        )
    }
});

ReactDOM.render(<App/>, document.getElementById('container'));