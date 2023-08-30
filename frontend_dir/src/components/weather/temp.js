import React, { useState,useEffect, useCallback } from "react";
import Weathercard from "./weathercard";
import "./style.css";

const Temp = () => {
  const [searchValue, setSearchValue] = useState("Bengaluru");
  const [tempInfo, setTempInfo] = useState({});

  const getWeatherInfo = useCallback(async (city) => {
    try {
      const response = await fetch(`http://54.197.97.97/get_weather?city=${searchValue}`);
      const data = await response.json();

      setTempInfo(data);
    } catch (error) {
      console.log(error);
    }
  }, [searchValue]);

  useEffect(() => {
    getWeatherInfo();
  }, []);

  return (
    <>
      <div className="wrap">
        <div className="search">
          <input
            type="search"
            placeholder="search..."
            autoFocus
            id="search"
            className="searchTerm"
            value={searchValue}
            onChange={(e) => setSearchValue(e.target.value)}
          />

          <button
            className="searchButton"
            type="button"
            onClick={getWeatherInfo}
          >
            Search
          </button>
        </div>
      </div>

      {/* our temp card  */}
      <Weathercard {...tempInfo} />
    </>
  );
};

export default Temp;

