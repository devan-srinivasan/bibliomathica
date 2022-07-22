import React, { Component } from "react";
import InputSubmit from "./InputSubmit.js";
class PuzzleDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = { submitted: "" };
  }

  handleSubmission(submission) {
    this.setState({ submitted: submission });
    console.log("PuzDis", submission);
  }

  render() {
    return (
      <div className="PuzzleDisplay">
        <h4>{this.props.title}</h4>
        <h6>
          <b>Question:</b> {this.props.question}
          <InputSubmit handleSubmission={this.handleSubmission.bind(this)} />
        </h6>
      </div>
    );
  }
}

export default PuzzleDisplay;
