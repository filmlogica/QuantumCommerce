export default function Home() {
  return (
    <main style={styles.container}>
      <h1 style={styles.header}>QuantumCommerce 2.0</h1>
      <p style={styles.tagline}>High-ticket automation powered by AI—ROI-first, always.</p>
      <a href="#waitlist" style={styles.button}>Join the Early Access List</a>
      <section style={styles.section}>
        <h2>Coming Soon</h2>
        <ul>
          <li>🚀 Dynamic AI-powered pricing engine</li>
          <li>🤖 Product selection that learns what sells</li>
          <li>💳 Stripe-backed subscription automation</li>
        </ul>
      </section>
    </main>
  )
}

const styles = {
  container: {
    fontFamily: 'sans-serif',
    padding: '2rem',
    maxWidth: '600px',
    margin: 'auto',
    textAlign: 'center'
  },
  header: {
    fontSize: '2.5rem'
  },
  tagline: {
    marginTop: '0.5rem',
    marginBottom: '2rem',
    fontSize: '1.2rem',
    color: '#666'
  },
  button: {
    display: 'inline-block',
    padding: '0.75rem 1.5rem',
    backgroundColor: '#111',
    color: '#fff',
    borderRadius: '5px',
    textDecoration: 'none',
    marginBottom: '2rem'
  },
  section: {
    textAlign: 'left'
  }
}
