# Style Guide — Why Does the Periodic Table Have a Maximum?

## Visual Identity

Inspired by **Kurzgesagt** and **3Blue1Brown** — clean, confident, educational but cinematic.

---

## Color Palette

### Primary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Background Dark** | `#0a0a0f` | `10, 10, 15` | Main background, slides |
| **White** | `#ffffff` | `255, 255, 255` | Primary text, titles |
| **Cyan Accent** | `#00e5ff` | `0, 229, 255` | Highlights, positive concepts, science keywords |

### Secondary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Gray Light** | `#a0a0a0` | `160, 160, 160` | Body text, descriptions |
| **Orange Warning** | `#ff6b35` | `255, 107, 53` | Problems, limitations, Coulomb repulsion |
| **Green Stable** | `#00ff88` | `0, 255, 136` | Stability, solutions, Island of Stability |

### Transparency Variants

```css
--cyan-glow: rgba(0, 229, 255, 0.3);      /* Glow effects */
--cyan-subtle: rgba(0, 229, 255, 0.1);    /* Subtle backgrounds */
--orange-glow: rgba(255, 107, 53, 0.3);   /* Warning glow */
--green-glow: rgba(0, 255, 136, 0.3);     /* Stability glow */
```

---

## Typography

### Primary Font
**Space Grotesk** (Google Fonts)

```css
font-family: 'Space Grotesk', sans-serif;
```

### Font Weights
| Weight | Value | Usage |
|--------|-------|-------|
| Light | 300 | Subtle text, captions |
| Regular | 400 | Body text |
| Medium | 500 | Emphasized text |
| SemiBold | 600 | Titles, headers |
| Bold | 700 | Numbers, stats |

### Font Sizes (Reveal.js Scale)

| Element | Size | Example |
|---------|------|---------|
| Main Title (H1) | 2.5em | Slide titles |
| Section Title (H2) | 1.8em | Content headers |
| Body Text | 1.1em | Paragraphs |
| Stat Numbers | 2em | Data callouts |
| Act Markers | 0.7em | Section labels |
| Captions | 0.8em | Descriptions |

---

## Animation Principles

### Timing Functions

```css
/* Smooth, organic movements */
transition: all 0.3s ease;

/* Energetic pulses */
animation: pulse 2s ease-in-out infinite;

/* Subtle attention */
animation: glow 2s ease-in-out infinite;

/* Urgent vibration */
animation: vibrate 0.1s linear infinite;
```

### Core Animations

#### 1. Pulse (Attention)
```css
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.8; transform: scale(1.05); }
}
```
*Use for: highlighted elements, current focus*

#### 2. Glow (Emphasis)
```css
@keyframes glow {
    0%, 100% { text-shadow: 0 0 20px var(--cyan-glow); }
    50% { text-shadow: 0 0 40px var(--cyan-accent), 0 0 60px var(--cyan-glow); }
}
```
*Use for: titles, key concepts, moments of discovery*

#### 3. Vibrate (Instability)
```css
@keyframes vibrate {
    0%, 100% { transform: translate(0, 0); }
    25% { transform: translate(1px, -1px); }
    50% { transform: translate(-1px, 1px); }
    75% { transform: translate(1px, 1px); }
}
```
*Use for: unstable nuclei, tension moments*

#### 4. Wave (Oscillation)
```css
@keyframes wave {
    0%, 100% { transform: scaleY(0.5); }
    50% { transform: scaleY(1.5); }
}
```
*Use for: resonance concepts, GDR visualization*

#### 5. Push (Force)
```css
@keyframes push {
    0% { transform: translateX(-10px); }
    100% { transform: translateX(10px); }
}
```
*Use for: force arrows, tug-of-war diagrams*

### Animation Guidelines

1. **Ease into motion** — Never start animations abruptly
2. **Match content tempo** — Faster for tension, slower for discovery
3. **Stagger delays** — Create visual rhythm with offset timings
4. **Pause at key frames** — Let important visuals breathe

---

## Visual Elements

### Unicode Symbols

| Symbol | Meaning | Usage |
|--------|---------|-------|
| ⚛ | Atom | General atomic concepts |
| ⬡ | Hexagon | Nucleus representation |
| 💥 | Explosion | Fission, instability |
| 🔬 | Microscope | Research, observation |
| 💡 | Light bulb | Discovery, solution |
| 🎵 | Music note | Resonance |
| 🔨 | Hammer | Brute force |
| ∞ | Infinity | Possibility, horizon |

### Nucleus Visualization

```css
.nucleus {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background: radial-gradient(circle, var(--cyan-accent) 0%, var(--bg-dark) 70%);
}
```

- **Stable**: Solid cyan gradient, no animation
- **Unstable**: Orange gradient, vibrate animation
- **Fusing**: Pulsing, size changing

### Force Diagrams

- **Strong Force**: Cyan arrows, pulling inward
- **Coulomb Repulsion**: Orange arrows, pushing outward
- **Equilibrium**: Arrows balanced, nucleus centered

### Data Boxes

```css
.stat-box {
    padding: 0.5em 1em;
    background: rgba(0, 229, 255, 0.1);
    border: 1px solid var(--cyan-accent);
}
```

- Number in **bold cyan**, label in **gray light**
- Animate numbers counting up for dramatic effect

---

## Slide Transitions

### Reveal.js Settings

```javascript
Reveal.initialize({
    transition: 'fade',
    transitionSpeed: 'slow',
    backgroundTransition: 'fade'
});
```

### Act Transitions
- Between acts: **2-second fade to black**, then fade in
- Within acts: **Standard fade** (0.5s)

### Element Transitions
- Text: Fade in from bottom
- Numbers: Count up animation
- Diagrams: Build piece by piece
- Highlights: Glow pulse then settle

---

## Layout Guidelines

### Slide Structure

```
┌─────────────────────────────────────────┐
│  [Act Marker - small, cyan, top-left]   │
│                                         │
│  ## Title (H2)                          │
│                                         │
│  Content area                           │
│  - Keep centered or left-aligned        │
│  - Maximum 3 bullet points              │
│  - One key visual per slide             │
│                                         │
│  [Visual/Animation - centered]          │
│                                         │
└─────────────────────────────────────────┘
```

### Spacing

- Margin from edges: 10%
- Title margin-bottom: 0.5em
- Content line-height: 1.6
- Visual margin: 1-2em

### Grid System

- Reveal.js default: 1280 × 720
- Content max-width: ~800px centered
- Side-by-side: 50/50 split with 2em gap

---

## Tone & Voice

### Visual Tone
- **Confident** — Bold statements, clear visuals
- **Educational** — Explain, don't overwhelm
- **Cinematic** — Dramatic pauses, reveals
- **Hopeful** — The horizon, not the wall

### Text Guidelines
- Short sentences
- Active voice
- Technical terms in **cyan accent**
- Problems in **orange warning**
- Solutions in **green stable**

---

## Asset Checklist

### For Full Animation Production

- [ ] Custom periodic table SVG (stylized, not realistic)
- [ ] Nucleus 3D model or 2D particle system
- [ ] Force arrow graphics (cyan/orange variants)
- [ ] NIF facility silhouette
- [ ] D-T fusion reaction sequence
- [ ] Island of Stability chart
- [ ] Wave/oscillation visualizations
- [ ] Thorium-229 energy diagram

### Audio Assets

- [ ] Ambient electronic drone (background)
- [ ] Laser/zap sound effects
- [ ] Tension building track
- [ ] Discovery/resolution chime
- [ ] Explosion sound
- [ ] Resonance/harmonic tones

---

## File Naming Convention

```
video/
├── SCRIPT.md              # Narration script
├── SHOT_LIST.md           # Shot-by-shot breakdown
├── STYLE_GUIDE.md         # This document
└── slides/
    └── index.html         # Reveal.js presentation
```

### For Production Assets (Future)

```
video/
├── assets/
│   ├── audio/
│   │   ├── voiceover.wav
│   │   ├── music_bed.wav
│   │   └── sfx/
│   ├── images/
│   │   ├── periodic_table.svg
│   │   └── nucleus/
│   └── animations/
│       ├── fusion_sequence.json
│       └── gdr_oscillation.json
```

---

## Reference Links

- **Kurzgesagt Style**: youtube.com/@kurzgesagt
- **3Blue1Brown Style**: youtube.com/@3blue1brown
- **Space Grotesk Font**: fonts.google.com/specimen/Space+Grotesk
- **Reveal.js**: revealjs.com
- **CSS Animation Guide**: developer.mozilla.org/en-US/docs/Web/CSS/animation
