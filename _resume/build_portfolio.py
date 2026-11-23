"""포트폴리오 PDF 생성

- 공개본: assets/kim-taehun-portfolio.pdf. 지원 기업 줄 없음, 웹에서 내려받기
- 제출본: _resume/out/kim-taehun-portfolio-submit.pdf. 지원 기업 줄 포함, 커밋 제외(.gitignore)
- 지원 기업 줄: _resume/submit.txt 한 줄(커밋 제외). 파일이 없으면 제출본 생략
- 목차 쪽 번호(@P1, @P2, @P3): 자리표시 0으로 1차 생성, PDF 이동 대상 쪽을 읽어 2차 생성
- 실행: python3 _resume/build_portfolio.py
"""
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SRC = os.path.join(ROOT, '_resume', 'portfolio.html')
TMP = os.path.join(ROOT, '_resume', '.portfolio-build.html')
PUBLIC = os.path.join(ROOT, 'assets', 'kim-taehun-portfolio.pdf')
SUBMIT = os.path.join(ROOT, '_resume', 'out', 'kim-taehun-portfolio-submit.pdf')
SUBMIT_LINE = os.path.join(ROOT, '_resume', 'submit.txt')


def render(html, out):
    with open(TMP, 'w', encoding='utf-8') as f:
        f.write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    '--virtual-time-budget=15000', f'--print-to-pdf={out}', f'file://{TMP}'],
                   stderr=subprocess.DEVNULL, check=True)
    data = open(out, 'rb').read()
    kids = [int(x) for x in re.findall(rb'(\d+) 0 R', re.search(rb'/Type\s*/Pages.*?/Kids\s*\[(.*?)\]', data, re.S).group(1))]
    dests = {k.decode(): int(v) for k, v in re.findall(rb'/(nuktu|ege|bustracker) \[(\d+) 0 R', data)}
    return {k: kids.index(v) + 1 for k, v in dests.items()}


def build(html, out):
    first = render(html.replace('@P1', '0').replace('@P2', '0').replace('@P3', '0'), out)
    final = html.replace('@P1', str(first['nuktu'])).replace('@P2', str(first['ege'])).replace('@P3', str(first['bustracker']))
    second = render(final, out)
    assert first == second, (first, second)
    return second


src = open(SRC, encoding='utf-8').read()
print('공개본 목차 쪽 번호', build(src.replace('<!-- @SUBMIT -->', ''), PUBLIC))
if os.path.exists(SUBMIT_LINE):
    line = open(SUBMIT_LINE, encoding='utf-8').read().strip()
    os.makedirs(os.path.dirname(SUBMIT), exist_ok=True)
    print('제출본 목차 쪽 번호', build(src.replace('<!-- @SUBMIT -->', f'<div class="apply"><b>지원</b>{line}</div>'), SUBMIT))
os.remove(TMP)
