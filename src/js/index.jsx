import React from "react";
import ReactDOM from "react-dom";
var Hello = React.createClass({
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

ReactDOM.render(<Hello />, document.getElementById('container'));