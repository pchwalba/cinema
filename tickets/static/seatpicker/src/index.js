import React, { Component } from "react";
import SeatPick from "./components/seatpick";
import ReactDOM from "react-dom";

class App extends Component {

  render() {
    return (
      <SeatPick />
    );
  }
}


const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
