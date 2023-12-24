// pages/index.js
import Link from 'next/link';

function Home() {
  return (
    <div>
      <h1>Home Page</h1>
      <Link href="/about">
        <a>About Page</a>
      </Link>
      <Link href="/contact">
        <a>Contact Page</a>
      </Link>
    </div>
  );
}

export default Home;
// pages/about.js

import React from 'react';

function About() {
  return (
    <div>
      <h1>About Page</h1>
      <p>This is the about page content.</p>
    </div>
  );
}

// ParentComponent.js
import React from 'react';
import ChildComponent from './ChildComponent';

function ParentComponent() {
  return <ChildComponent name="John" />;
}

export default ParentComponent;

// ChildComponent.js
import React from 'react';

function ChildComponent(props) {
  return <p>Hello, {props.name}!</p>;
}

export default ChildComponent;




  import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}

export default Counter;


import React from 'react';

function ConditionalRender(props) {
  return (
    <div>
      {props.isLoggedIn ? <p>Welcome, User!</p> : <p>Please log in.</p>}
    </div>
  );
}

export default ConditionalRender;



import React, { useState } from 'react';

function MyForm() {
  const [inputValue, setInputValue] = useState('');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  return (
    <form>
      <input type="text" value={inputValue} onChange={handleChange} />
      <p>You typed: {inputValue}</p>
    </form>
  );
}

export default MyForm;



import { createContext } from 'react';

const DataContext = createContext();

export default DataContext;


// DataProvider.js
import React, { useState } from 'react';
import DataContext from './DataContext';

const DataProvider = ({ children }) => {
  const [data, setData] = useState(initialData);

  return (
    <DataContext.Provider value={{ data, setData }}>
      {children}
    </DataContext.Provider>
  );
};

export default DataProvider;


// SomeComponent.js
import React, { useContext } from 'react';
import DataContext from './DataContext';

function SomeComponent() {
  const { data, setData } = useContext(DataContext);

  return (
    <div>
      <p>Data: {data}</p>
      <button onClick={() => setData('Updated data')}>Update Data</button>
    </div>
  );
}



import React, { useState, useEffect } from 'react';

function DataFetching() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Fetch data from an API
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []); // Empty dependency array means this effect runs once, similar to componentDidMount

  return (
    <div>
      {data ? <p>Data: {data}</p> : <p>Loading...</p>}
    </div>
  );
}



import React, { useRef, useEffect } from 'react';

function FocusInput() {
  const inputRef = useRef(null);

  useEffect(() => {
    // Focus the input element when the component mounts
    inputRef.current.focus();
  }, []);

  return <input ref={inputRef} />;
}


import React, { useRef } from 'react';

function MyComponent() {
  // Using useRef to store a value that doesn't trigger re-renders
  const someValueRef = useRef('Initial Value');

  const handleClick = () => {
    // Modifying the value stored in useRef
    someValueRef.current = 'Updated Value';
    // This won't trigger a re-render
  };

  return (
    <div>
      <p>Value stored in useRef: {someValueRef.current}</p>
      <button onClick={handleClick}>Update Value</button>
    </div>
  );
}

export default MyComponent;
