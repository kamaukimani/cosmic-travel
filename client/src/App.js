import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Dashboard from './components/Dashboard'
import ScientistDetail from './components/ScientistDetail'

function App() {
  return (
    <div>
      <Header />

      <main>
        <Routes>
          <Route index element={<Dashboard />} />
          <Route
            path="/scientists/:id/*"
            element={<ScientistDetail />}
          />
          <Route
            path="*"
            element={<h2>404 - Page Not Found</h2>}
          />
        </Routes>
      </main>

      <footer>
        <p>Scientist Dashboard © 2026</p>
      </footer>
    </div>
  )
}

export default App