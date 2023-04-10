import logo from './logo.svg';
import './App.css';

function App() {
  const displayQuestions = false;
  const questions = "\n\n1. What other hobbies do you have?\n2. What do you like to do in your free time?\n3. What do you think about the current state of the world?\n4. What do you think are the biggest challenges facing society today?\n5. What do"
  return (
    <div className="App">
      <header className="App-header">
        <h1>Awkward Silence No More</h1>
        <h4>Coming Soon</h4>
        {
          displayQuestions && (
            <div dangerouslySetInnerHTML={{__html: questions}} />
          )
        }
        <p>Created by Vilde Vevatne</p>
      </header>
    </div>
  );
}

export default App;
