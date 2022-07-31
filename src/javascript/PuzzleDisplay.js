import React, { Component } from "react";
import InputSubmit from "./InputSubmit.js";

class PuzzleDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = { correct_answer: "" };
    this.handleSubmission = this.handleSubmission.bind(this);
  }

  handleSubmission(submission) {
    fetch(
      "http://localhost:8000/check_answer/?title=" +
        this.props.title +
        "&answer=" +
        submission,
      {
        method: "GET"
      }
    )
      .then(function (response) {
        return response.json();
      })
      .then((data) => {
        this.setState({ correct_answer: data.result });
      });
  }

  render() {
    return (
      <div className="PuzzleDisplay">
        <h4>{this.props.title}</h4>
        <h6>
          <b>Question:</b> {this.props.question}
          <InputSubmit
            color={this.state.correct_answer}
            handleSubmission={this.handleSubmission.bind(this)}
          />
        </h6>
      </div>
    );
  }
}

export default PuzzleDisplay;
