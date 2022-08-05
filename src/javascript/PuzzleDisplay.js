import React, { Component } from "react";
import InputSubmit from "./InputSubmit.js";
import "./react-stylesheets/PuzzleDisplay.css";
import web_config from "./config.js";

class PuzzleDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      correct_answer: "init",
      title: this.props.title,
      question: this.props.question,
      last_submission: ""
    };
    this.handleSubmission = this.handleSubmission.bind(this);
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.props.title !== prevProps.title) {
      this.setState({
        correct_answer: "init",
        title: this.props.title,
        question: this.props.question
      });
    }
  }

  async handleSubmission(submission) {
    if (web_config.mode == "dev") {
      host_address = web_config.dev.address + ":" + web_config.dev.port;
    } else {
      host_address = web_config.prod.address;
    }
    await fetch(
       host_address + "/check_answer/?title=" +
        this.state.title +
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
    this.setState({ last_submission: submission });
  }

  render() {
    var result;
    if (this.state.correct_answer === "True") {
      result = (
        <>
          <p className="correct">{this.state.last_submission}: correct!</p>
        </>
      );
    } else if (this.state.correct_answer === "False") {
      result = (
        <>
          <p className="wrong">{this.state.last_submission}: wrong!</p>
        </>
      );
    } else if (this.state.correct_answer === "init") {
      result = (
        <>
          <p className="init">submit an answer</p>
        </>
      );
    }
    return (
      <div className="PuzzleDisplay">
        <h3>Puzzle: {this.state.title}</h3>
        <h5>
          <u>Question:</u> {this.state.question}
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
