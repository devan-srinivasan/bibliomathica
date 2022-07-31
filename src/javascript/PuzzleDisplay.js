import React, { Component } from "react";
import InputSubmit from "./InputSubmit.js";

class PuzzleDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      correct_answer: "init",
      title: this.props.title,
      question: this.props.question
    };
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
    var result;
    console.log(this.state.correct_answer);
    if (this.state.correct_answer === "True") {
      result = <p>correct!</p>;
    } else if (this.state.correct_answer === "False") {
      result = <p>wrong!</p>;
    } else if (this.state.correct_answer === "init") {
      result = <p>submit an answer!</p>;
    }
    return (
      <div className="PuzzleDisplay">
        <h3>Puzzle: {this.props.title}</h3>
        <h5>
          <u>Question:</u> {this.props.question}
        </h5>
        <h5>
          <u>Answer:</u>
          <InputSubmit handleSubmission={this.handleSubmission.bind(this)} />
        </h5>
        {result}
      </div>
    );
  }
}

export default PuzzleDisplay;
