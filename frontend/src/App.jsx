import {useEffect, useState} from "react";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import About from "./components/About";
import Projects from "./components/Projects";
import Experience from "./components/Experience";
import Skills from "./components/Skills";
import AvatarAssistant from "./components/AvatarAssistant";

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
  );
}

export default App;