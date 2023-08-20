import React, { Component } from "react";
import NewTicketForm from './ticket_form'
import SeatPicker from "react-seat-picker";
import axios from "axios";
import { API_URL } from "../constants";


class SeatPick extends Component {
    constructor(props) {
        super(props);
        this.state = false

    }

  componentDidMount() {
    axios.get(API_URL).then(res =>
        {
             this.setState({
                 screening: res.data.screening,
                 booked: res.data.booked,
                 loading: false});
        });

  }

  addSeatCallback = ({ row, number, id }, addCb) => {
    this.setState(
      {
        loading: true
      },
      async () => {
        await new Promise(resolve => setTimeout(resolve, 15));
        console.log(`Added seat ${number}, row ${row}, id ${id}`);
        this.setState({ seat: id })
        addCb(row, number, id);
        this.setState({ loading: false });
      }
    );
  };

  removeSeatCallback = ({ row, number, id }, removeCb) => {
    this.setState(
      {
        loading: true
      },
      async () => {
        await new Promise(resolve => setTimeout(resolve, 15));
        console.log(`Removed seat ${number}, row ${row}, id ${id}`);
        removeCb(row, number);
        this.setState({ loading: false });
      }
    );
  };

  createSeats() {
    const numberOfCols = [21,23,24,25,25,25,25,25,25,25,22,26,25,26,26,25,25,19];
    const rows = []
    var bookedSeats = [];
    if (this.state.booked){
        bookedSeats = this.state.booked
        };
    console.log(API_URL)
    let id = 1
    numberOfCols.forEach((row)=> {
      let tempRow = []
      for(let i=1; i<=row; i++){
        let number = i
        if (bookedSeats.includes(id)){
           tempRow.push({id, number,isReserved: true })
        }else {
            tempRow.push({id, number, })
        }
        id++
      }
      rows.push(tempRow)
    });
    return rows
    };

  render() {
    return (
      <div>
        <div style={{ marginTop: "10px" }}>
          <SeatPicker
            addSeatCallback={this.addSeatCallback}
            removeSeatCallback={this.removeSeatCallback}
            rows={this.createSeats()}
            maxReservableSeats={1}
            alpha
            visible
            selectedByDefault
            loading={this.state.loading}
          />
           <NewTicketForm ticket_info={this.state} />
        </div>

      </div>
    );
  }
}

export default SeatPick