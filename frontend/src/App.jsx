
import { useState } from "react";
import {
  Search,
  BriefcaseBusiness,
  MapPin,
  Sparkles,
  Code2,
  ArrowUpRight,
  LoaderCircle,
  Target,
  BrainCircuit,
  TrendingUp
} from "lucide-react";

import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [jobs, setJobs] = useState([]);
  const [details, setDetails] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Search jobs using FastAPI backend
  const searchJobs = async () => {
    if (!query.trim()) {
      setError("Please describe the job you are looking for.");
      return;
    }

    setLoading(true);
    setError("");
    setJobs([]);
    setDetails(null);

    try {
      const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const response = await fetch(
  `${API_URL}/find-jobs`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            request: query
          })
        }
      );

      if (!response.ok) {
        throw new Error("Unable to fetch jobs. Please try again.");
      }

      const data = await response.json();

      setJobs(data.recommended_jobs || []);
      setDetails(data.extracted_details || {});

      if (!data.recommended_jobs?.length) {
        setError("No matching jobs found. Try another search.");
      }

    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  const formatScore = (score) => {
    return `${Math.round((score || 0) * 100)}%`;
  };

  return (
    <div className="app">

      {/* Navigation */}
      <nav className="navbar">

        <div className="brand">
          <div className="brand-icon">
            <BrainCircuit size={23} />
          </div>

          <span>
            Career<span className="brand-highlight">AI</span>
          </span>
        </div>

        <div className="nav-right">
          <span className="status-dot"></span>
          <span>AI Engine Active</span>
          <div className="avatar">AI</div>
        </div>

      </nav>

      <main className="main-container">

        {/* Hero Section */}
        <section className="hero">

          <div className="eyebrow">
            <Sparkles size={15} />
            <span>SMART CAREER DISCOVERY</span>
          </div>

          <h1>
            Find your next
            <br />
            <span>opportunity with AI.</span>
          </h1>

          <p className="hero-description">
            Tell us about your skills and career goals.
            Our AI will find jobs that match your profile.
          </p>

          {/* Search Box */}
          <div className="search-box">

            <div className="search-input-area">
              <Search size={21} />

              <input
                type="text"
                placeholder="Describe your skills, preferred job and location..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === "Enter") searchJobs();
                }}
              />
            </div>

            <button
              className="search-button"
              onClick={searchJobs}
              disabled={loading}
            >
              {loading ? (
                <LoaderCircle className="spin" size={19} />
              ) : (
                <Search size={18} />
              )}

              {loading ? "Searching..." : "Find Jobs"}
            </button>

          </div>

          <div className="search-hint">
            <span>Try:</span>

            <button
              onClick={() =>
                setQuery(
                  "I know Python and SQL. I want a data analyst internship in Delhi."
                )
              }
            >
              Data Analyst Intern
            </button>

            <button
              onClick={() =>
                setQuery(
                  "I know C++, DSA and Python. I want a junior software developer job in Bangalore."
                )
              }
            >
              Junior Developer
            </button>
          </div>

        </section>

        {/* Features */}
        <section className="feature-grid">

          <div className="feature-card">
            <div className="feature-icon purple">
              <BrainCircuit size={21} />
            </div>

            <div>
              <h3>AI Powered</h3>
              <p>Understands natural language</p>
            </div>
          </div>

          <div className="feature-card">
            <div className="feature-icon blue">
              <Target size={21} />
            </div>

            <div>
              <h3>Smart Matching</h3>
              <p>Semantic job recommendations</p>
            </div>
          </div>

          <div className="feature-card">
            <div className="feature-icon green">
              <TrendingUp size={21} />
            </div>

            <div>
              <h3>Personalized</h3>
              <p>Matches your career goals</p>
            </div>
          </div>

        </section>

        {/* Error Message */}
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {/* Results */}
        {details && (
          <section className="results-section">

            <div className="results-heading">

              <div>
                <div className="section-label">
                  <Sparkles size={15} />
                  AI ANALYSIS
                </div>

                <h2>Your job matches</h2>

                <p>
                  Recommendations based on your search.
                </p>
              </div>

              <div className="result-count">
                {jobs.length} Jobs Found
              </div>

            </div>

            {/* Extracted Details */}
            <div className="details-panel">

              <h3>What we understood</h3>

              <div className="detail-tags">

                {(details.skills || []).map((skill, index) => (
                  <span className="tag" key={index}>
                    <Code2 size={13} />
                    {skill}
                  </span>
                ))}

                {details.level && (
                  <span className="tag">
                    {details.level}
                  </span>
                )}

                {details.location && (
                  <span className="tag">
                    <MapPin size={13} />
                    {details.location}
                  </span>
                )}

              </div>

            </div>

            {/* Job Cards */}
            <div className="job-list">

              {jobs.map((job) => (
                <article
                  className="job-card"
                  key={job.job_id}
                >

                  <div className="job-top">

                    <div className="company-icon">
                      <BriefcaseBusiness size={23} />
                    </div>

                    <div className="job-title-area">
                      <h3>{job.title}</h3>
                      <p>{job.company}</p>
                    </div>

                    <div className="match-score">
                      <strong>
                        {formatScore(job.similarity)}
                      </strong>
                      <span>Match score</span>
                    </div>

                  </div>

                  <div className="job-meta">

                    <span>
                      <MapPin size={15} />
                      {job.location}
                    </span>

                    <span>
                      <BriefcaseBusiness size={15} />
                      {job.experience_level}
                    </span>

                    <span className="job-id">
                      Job #{job.job_id}
                    </span>

                  </div>

                  <div className="explanation">

                    <div className="explanation-title">
                      <Sparkles size={15} />
                      Why this matches
                    </div>

                    <p>{job.explanation}</p>

                  </div>

                  <div className="job-footer">
                    <span>Recommended by CareerAI</span>
                    <ArrowUpRight size={18} />
                  </div>

                </article>
              ))}

            </div>

          </section>
        )}

        {/* Empty State */}
        {!details && !loading && (

          <section className="empty-state">

            <div className="empty-icon">
              <BriefcaseBusiness size={30} />
            </div>

            <h2>Your next opportunity starts here.</h2>

            <p>
              Enter your skills, preferred role and location
              to discover matching jobs.
            </p>

            <div className="empty-decoration">
              <span></span>
              <span></span>
              <span></span>
            </div>

          </section>

        )}

        {/* Loading */}
        {loading && (

          <div className="loading-state">

            <LoaderCircle className="spin" size={30} />

            <h3>
              AI is finding your opportunities...
            </h3>

            <p>
              Analyzing skills and matching job descriptions.
            </p>

          </div>

        )}

      </main>

      {/* Footer */}
      <footer>
        <span>© 2026 CareerAI</span>
        <span>Built with AI · FastAPI · React</span>
      </footer>

    </div>
  );
}

export default App;
