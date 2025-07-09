import profilepic from './assets/profilepic.jpg'

 function Card() {

  return (
    <div className="card">
       <img className="card-image" src={profilepic} alt="profile picture"></img>
       <h2>Matthew Publico</h2>
       <p>I am a University Student in Computer Science</p>
    </div>
    );
 }

 export default Card