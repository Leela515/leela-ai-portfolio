import {useEffect, useState} from "react";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import About from "./components/About";
import Projects from "./components/Projects";
import Experience from "./components/Experience";
import Skills from "./components/Skills";
import AvatarAssistant from "./components/AvatarAssistant";

import "./styles/background.css";
import "./styles/glass.css";
import "./styles/animation.css";


function App() {
  const [ showNavbar, setShowNavbar ] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setShowNavbar(window.scrollY > 120);
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    }
  }, []);

  return (
    <>
      {/* Animated background */}
      <div className="background">
        <div className="blob blob1"></div>
        <div className="blob blob2"></div>
        <div className="blob blob3"></div>
      </div>
      <div className="app">
        {showNavbar && <Navbar />}

        <main>
          <Hero />
          <About />
          <Projects />
          <Experience />
          <Skills />
        </main>

        <AvatarAssistant />
      </div>
    </>
  );
}

export default App;