// Copyright (C) 2026 Luis Henrique Cassis Fagundes. AGPL-3.0-or-later.
import React from 'react';
import {Slot, defineElement, defineSet} from 'videomaker/stage';
import './stage.css';

function PortraitStage() {
  return <div className="portrait-page">
    <Slot name="machine" className="portrait-machine"/>
    <Slot name="copy" className="portrait-copy"/>
    <Slot name="note" className="portrait-note"/>
  </div>;
}
function CreditStage() {
  return <div className="credit-page"><Slot name="roll" className="credit-slot"/></div>;
}
function Panel({state}) {
  const p = state.props;
  return <section className={'panel panel-' + p.variant}>
    <div className="eyebrow">{p.eyebrow}</div>
    <h1>{p.title}</h1><div className="accent-rule"/>
    <p className="deck">{p.body}</p>
    <div className="facts">{p.items.map((item, i) =>
      <div className="fact" key={i}><span className="fact-dot"/>{item}</div>)}</div>
  </section>;
}
function Footnote({state}) {
  return <div className="footnote"><span>{state.props.left}</span><span>{state.props.right}</span></div>;
}
function CreditRoll({state}) {
  const p = state.props;
  const progress = state.actions.find(a => a.action === 'roll')?.progress ?? 0;
  // Every group has a declared, fixed screen-height unit; no DOM measurement,
  // wall clock, CSS animation or remembered frame influences the roll.
  const travel = p.groups.length * p.groupHeight + p.travelExtra;
  const y = p.startY - progress * travel;
  return <section className="credits">
    <header><span>{p.eyebrow}</span><h1>{p.title}</h1></header>
    <div className="roll-window">
      <div className="roll-content" style={{transform: 'translateY(' + y + 'vh)'}}>
        {p.groups.map((g, i) => <section className="credit-group" key={i}
            style={{height: p.groupHeight + 'vh'}}>
          <h2>{g.role}</h2><div className="credit-names">{g.names}</div>
          {g.lines.map((line, j) => <div className="credit-line" key={j}>{line}</div>)}
        </section>)}
      </div>
    </div>
    <footer>{p.footer}</footer>
  </section>;
}
defineSet({kind:'portrait-stage', slots:['machine','copy','note'], component:PortraitStage});
defineSet({kind:'credit-stage', slots:['roll'], component:CreditStage});
defineElement({kind:'panel', component:Panel});
defineElement({kind:'footnote', component:Footnote});
defineElement({kind:'credit-roll', component:CreditRoll});
