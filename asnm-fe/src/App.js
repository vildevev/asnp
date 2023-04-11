import "./App.css";
import AudioRecorder from "../src/AudioRecorder";

const App = () => {
    return (
        <div>
            <h1 className="title">Awkward Silence No More</h1>
            <div>
                {<AudioRecorder />}
            </div>
        </div>
    );
};
export default App;