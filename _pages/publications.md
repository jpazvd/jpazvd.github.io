---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
description: "Publications by João Pedro Azevedo: 144+ works on Learning Poverty, education economics, poverty measurement. Includes Lancet, World Development articles."
---

{% include base_path %}

<!-- Citation Metrics Banner -->
<div class="citation-metrics" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <h3 style="margin-top: 0; color: white; border-bottom: 1px solid rgba(255,255,255,0.3); padding-bottom: 0.5rem;">📊 Citation & Impact Metrics</h3>
  <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-around;">
    <div style="text-align: center;">
      <div style="font-size: 2rem; font-weight: bold;">{{ site.data.citations.google_scholar.total_citations | default: '5,500+' }}</div>
      <div style="font-size: 0.85rem; opacity: 0.9;">Total Citations</div>
    </div>
    <div style="text-align: center;">
      <div style="font-size: 2rem; font-weight: bold;">{{ site.data.citations.google_scholar.h_index | default: '30' }}</div>
      <div style="font-size: 0.85rem; opacity: 0.9;">h-index</div>
    </div>
    <div style="text-align: center;">
      <div style="font-size: 2rem; font-weight: bold;">{{ site.data.citations.google_scholar.i10_index | default: '62' }}</div>
      <div style="font-size: 0.85rem; opacity: 0.9;">i10-index</div>
    </div>
    <div style="text-align: center;">
      <div style="font-size: 2rem; font-weight: bold;">{{ site.data.citations.repec.total_works | default: '84' }}</div>
      <div style="font-size: 0.85rem; opacity: 0.9;">RePEc Works</div>
    </div>
    <div style="text-align: center;">
      <div style="font-size: 2rem; font-weight: bold;">{{ site.data.citations.repec.total_downloads_all_time | default: '32,000+' }}</div>
      <div style="font-size: 0.85rem; opacity: 0.9;">Total Downloads</div>
    </div>
  </div>
  <div style="margin-top: 1rem; font-size: 0.8rem; opacity: 0.8; text-align: center;">
    <a href="{{ site.data.citations.google_scholar.profile_url }}" target="_blank" style="color: white;">Google Scholar</a> | 
    <a href="{{ site.data.citations.repec.profile_url }}" target="_blank" style="color: white;">RePEc/IDEAS</a> | 
    <a href="{{ site.data.citations.orcid.profile_url }}" target="_blank" style="color: white;">ORCID</a>
    <br>Last updated: {{ site.data.citations.google_scholar.last_updated }}
  </div>
</div>

<!-- Publication Outlets & Impact Factors -->
<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin-bottom: 2rem; border-left: 4px solid #667eea;">
  <h3 style="margin-top: 0;">📰 Selected Publication Outlets</h3>
  <p style="margin-bottom: 1rem; color: #666;">Publications in high-impact peer-reviewed journals and policy outlets:</p>
  
  <table style="width: 100%; border-collapse: collapse; font-size: 0.9rem;">
    <thead>
      <tr style="background: #e9ecef;">
        <th style="padding: 10px; text-align: left; border-bottom: 2px solid #dee2e6;">Journal / Outlet</th>
        <th style="padding: 10px; text-align: center; border-bottom: 2px solid #dee2e6;">Impact Factor</th>
        <th style="padding: 10px; text-align: center; border-bottom: 2px solid #dee2e6;">Category</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px; border-bottom: 1px solid #dee2e6;"><strong>The Lancet</strong></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;"><span style="background: #28a745; color: white; padding: 2px 8px; border-radius: 4px;">168.9</span></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;">Medical</td>
      </tr>
      <tr style="background: #f8f9fa;">
        <td style="padding: 10px; border-bottom: 1px solid #dee2e6;"><strong>World Development</strong></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;"><span style="background: #17a2b8; color: white; padding: 2px 8px; border-radius: 4px;">5.3</span></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;">Development Economics</td>
      </tr>
      <tr>
        <td style="padding: 10px; border-bottom: 1px solid #dee2e6;"><strong>World Bank Research Observer</strong></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;"><span style="background: #17a2b8; color: white; padding: 2px 8px; border-radius: 4px;">4.2</span></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;">Economics</td>
      </tr>
      <tr style="background: #f8f9fa;">
        <td style="padding: 10px; border-bottom: 1px solid #dee2e6;"><strong>CEPAL Review</strong></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;"><span style="background: #6c757d; color: white; padding: 2px 8px; border-radius: 4px;">0.8</span></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;">Development Policy</td>
      </tr>
      <tr>
        <td style="padding: 10px; border-bottom: 1px solid #dee2e6;"><strong>World Bank Economic Premise</strong></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;"><span style="background: #6c757d; color: white; padding: 2px 8px; border-radius: 4px;">Policy</span></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;">Policy Brief</td>
      </tr>
      <tr style="background: #f8f9fa;">
        <td style="padding: 10px; border-bottom: 1px solid #dee2e6;"><strong>World Bank Policy Research Working Papers</strong></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;"><span style="background: #6c757d; color: white; padding: 2px 8px; border-radius: 4px;">WP</span></td>
        <td style="padding: 10px; text-align: center; border-bottom: 1px solid #dee2e6;">Working Papers</td>
      </tr>
    </tbody>
  </table>
  <p style="font-size: 0.8rem; color: #888; margin-top: 0.5rem; margin-bottom: 0;"><em>Impact factors from 2024 Journal Citation Reports (Clarivate)</em></p>
</div>

<!-- Publication Breakdown by Type -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
  <div style="background: #fff; padding: 1rem; border-radius: 8px; border: 1px solid #e9ecef; text-align: center;">
    <div style="font-size: 2rem; font-weight: bold; color: #667eea;">{{ site.data.citations.repec.journal_articles.count | default: '7' }}</div>
    <div style="font-size: 0.9rem; color: #666;">Peer-Reviewed Articles</div>
  </div>
  <div style="background: #fff; padding: 1rem; border-radius: 8px; border: 1px solid #e9ecef; text-align: center;">
    <div style="font-size: 2rem; font-weight: bold; color: #764ba2;">{{ site.data.citations.repec.working_papers.count | default: '50' }}</div>
    <div style="font-size: 0.9rem; color: #666;">Working Papers</div>
  </div>
  <div style="background: #fff; padding: 1rem; border-radius: 8px; border: 1px solid #e9ecef; text-align: center;">
    <div style="font-size: 2rem; font-weight: bold; color: #28a745;">{{ site.data.citations.repec.books.count | default: '3' }}</div>
    <div style="font-size: 0.9rem; color: #666;">Books</div>
  </div>
  <div style="background: #fff; padding: 1rem; border-radius: 8px; border: 1px solid #e9ecef; text-align: center;">
    <div style="font-size: 2rem; font-weight: bold; color: #17a2b8;">{{ site.data.citations.repec.software.count | default: '22' }}</div>
    <div style="font-size: 0.9rem; color: #666;">Software Modules</div>
  </div>
</div>

<!-- Rankings -->
<div style="background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%); padding: 1.5rem; border-radius: 8px; margin-bottom: 2rem;">
  <h3 style="margin-top: 0;">🏆 RePEc Rankings</h3>
  <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-around;">
    <div style="text-align: center; background: white; padding: 1rem; border-radius: 8px; min-width: 150px;">
      <div style="font-size: 1.5rem; font-weight: bold; color: #667eea;">#{{ site.data.citations.repec.rankings.software_global.rank_total_downloads | default: '19' }}</div>
      <div style="font-size: 0.8rem; color: #666;">Software Downloads<br>(Global)</div>
    </div>
    <div style="text-align: center; background: white; padding: 1rem; border-radius: 8px; min-width: 150px;">
      <div style="font-size: 1.5rem; font-weight: bold; color: #764ba2;">#{{ site.data.citations.repec.rankings.software_us.rank_total_downloads | default: '6' }}</div>
      <div style="font-size: 0.8rem; color: #666;">Software Downloads<br>(US)</div>
    </div>
    <div style="text-align: center; background: white; padding: 1rem; border-radius: 8px; min-width: 150px;">
      <div style="font-size: 1.5rem; font-weight: bold; color: #28a745;">Top 5%</div>
      <div style="font-size: 0.8rem; color: #666;">Authors by<br>Downloads</div>
    </div>
  </div>
</div>

<hr style="margin: 2rem 0;">

<h2>📚 Full Publication Profiles</h2>

<ul>
  <li><a href="https://scholar.google.com/citations?user=lTKXA78AAAAJ" target="_blank"><strong>Google Scholar</strong></a> — Complete citation record ({{ site.data.citations.google_scholar.total_citations }} citations)</li>
  <li><a href="https://ideas.repec.org/e/pwa88.html" target="_blank"><strong>RePEc/IDEAS</strong></a> — Working papers, articles, and software ({{ site.data.citations.repec.total_works }} works)</li>
  <li><a href="https://openknowledge.worldbank.org/entities/person/360f7a2e-0784-56e1-acf4-7f805fd50257" target="_blank"><strong>World Bank Open Knowledge Repository</strong></a> — Official World Bank publications ({{ site.data.citations.world_bank_okr.publication_count }} publications)</li>
  <li><a href="https://orcid.org/0000-0003-2111-0596" target="_blank"><strong>ORCID</strong></a> — Persistent author identifier</li>
</ul>

<hr style="margin: 2rem 0;">

<h2>🔬 Selected High-Impact Publications</h2>

<h3>Peer-Reviewed Journal Articles</h3>

<ol>
  <li><strong>Azevedo, JP</strong>, Hasan, A, Goldemberg, D, Geven, K, Iqbal, SA (2021). <a href="https://doi.org/10.1093/wbro/lkab003" target="_blank">"Simulating the Potential Impacts of COVID-19 School Closures on Schooling and Learning Outcomes: A Set of Global Estimates."</a> <em>The World Bank Research Observer</em>, 36(1), 1-40. <span style="background: #17a2b8; color: white; padding: 1px 6px; border-radius: 3px; font-size: 0.8rem;">IF: 4.2</span></li>
  
  <li>Castañeda, A, Doan, D, Newhouse, D, Nguyen, MC, Uematsu, H, <strong>Azevedo, JP</strong> (2018). <a href="https://doi.org/10.1016/j.worlddev.2017.08.002" target="_blank">"A New Profile of the Global Poor."</a> <em>World Development</em>, 101, 250-267. <span style="background: #17a2b8; color: white; padding: 1px 6px; border-radius: 3px; font-size: 0.8rem;">IF: 5.3</span></li>
  
  <li>Andalón, M, <strong>Azevedo, JP</strong>, Rodríguez-Castelán, C, Sanfelice, V, Valderrama-González, D (2016). <a href="https://doi.org/10.1016/j.worlddev.2015.12.020" target="_blank">"Weather Shocks and Health at Birth in Colombia."</a> <em>World Development</em>, 82, 69-82. <span style="background: #17a2b8; color: white; padding: 1px 6px; border-radius: 3px; font-size: 0.8rem;">IF: 5.3</span></li>
</ol>

<h3>World Bank Flagship Publications</h3>

<ol>
  <li><strong>Azevedo, JP</strong>, et al. (2021). <a href="https://www.worldbank.org/en/topic/education/publication/state-of-global-learning-poverty" target="_blank">"Learning Poverty: Measures and Simulations."</a> <em>World Bank Policy Research Working Paper</em> No. 9446.</li>
  
  <li><strong>Azevedo, JP</strong>, et al. (2020). <a href="https://openknowledge.worldbank.org/handle/10986/34654" target="_blank">"Simulating the Potential Impacts of COVID-19 School Closures on Schooling and Learning Outcomes."</a> <em>World Bank Policy Research Working Paper</em> No. 9284.</li>
</ol>

<p style="margin-top: 2rem; font-size: 0.9rem; color: #666;"><em>For a complete list of publications, please visit my <a href="https://scholar.google.com/citations?user=lTKXA78AAAAJ" target="_blank">Google Scholar</a> or <a href="https://ideas.repec.org/e/pwa88.html" target="_blank">RePEc</a> profiles.</em></p>
