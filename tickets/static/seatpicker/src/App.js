import React from "react";
import SeatPick from "./components/seatpick";
import ReactDOM from "react-dom";
import { BrowserRouter,Router } from 'react-router-dom'

class App extends React.Component {

  render() {
    return (
        <SeatPick />
    );
  }
}


const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
