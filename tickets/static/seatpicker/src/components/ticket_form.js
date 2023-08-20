import React, { Component } from "react";
import axios from "axios";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";
import { API_POST } from "../constants";
import { useNavigate, redirect } from 'react-router-dom';

class NewTicketForm extends Component {

  state = { name: "",
    phone_number: "",
    email: "",
    screening: "",
    seat: "",
    discount: "false",
  };





  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createTicket = e => {

    e.preventDefault();
    this.state.seat = this.props.ticket_info.seat;
    this.state.screening = this.props.ticket_info.screening;
    axios.post(API_POST, this.state).then(response => {
                     window.location = "/ticket/" + response.data.id
                   });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {


    return (
      <div class="form">
      <Form onSubmit={ this.createTicket }>
        <FormGroup>
          <Label for="name">Name:</Label>
          <Input
            type="text"
            name="name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.name)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="email">Email:</Label>
          <Input
            type="email"
            name="email"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.email)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="phone">Phone:</Label>
          <Input
            type="text"
            name="phone_number"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.phone_number)}
          />
        </FormGroup>
        <FormGroup>
            <Label for="discount">Discount:</Label>
            <Input
              type="checkbox"
              name="discount"
              onChange={this.onChange}
              value={this.defaultIfEmpty(this.state.discount)}
            />
        </FormGroup>
        <FormGroup>
            <Input
              type="hidden"
              name="seat"
              onChange={this.onChange}
              value={this.defaultIfEmpty(this.props.seat)}
            />
        </FormGroup>
        <Button>Send</Button>
      </Form>
      </div>
    );
  }
}

export default NewTicketForm;