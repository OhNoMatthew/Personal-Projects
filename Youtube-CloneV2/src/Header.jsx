import logo from './assets/youtoob.jpg'

function Header(){

    return(
      <header>
        <h1>YouTube Clone V2</h1>
        <img src={logo} alt="website logo" href="Home.jsx"></img>
        <nav>
          <ul>
            <li><a href="#"></a>Home</li>
            <li><a href="#"></a>Login</li>
            <li><a href="#"></a>Post</li>
            <li><a href="#"></a>View Profile</li>
          </ul>
        </nav>
        <hr></hr>
      </header>
    );
}

export default Header