import React, { Component } from "react";
import "./react-stylesheets/InputSubmit.css";

class InputSubmit extends Component {
  constructor(props) {
    super(props);
    this.state = {
      submitted: "0"
    };
  }

  handleChange(event) {
    this.setState({ submitted: event.target.value });
  }

  render() {
    return (
      <div className="InputSubmit">
        <input
          type="text"
          id="message"
          name="message"
          onChange={this.handleChange.bind(this)}
          value={this.state.submitted}
          autoComplete="off"
          text=""
        />

        <button
          onClick={() =>
            this.props.handleSubmission(this.state.submitted.toString())
          }
        >
          Submit
        </button>
      </div>
    );
  }
}

export default InputSubmit;
