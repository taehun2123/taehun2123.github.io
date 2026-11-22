"""포트폴리오 PDF 생성

- 목적: 1쪽 목차 표의 쪽 번호(@P1, @P2, @P3)를 실제 PDF 쪽으로 채움
- 방법: 자리표시 0으로 1차 생성, PDF 이동 대상(nuktu, ege, bustracker) 쪽을 읽어 2차 생성
- 실행: python3 _resume/build_portfolio.py
"""
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SRC = os.path.join(ROOT, '_resume', 'portfolio.html')
TMP = os.path.join(ROOT, '_resume', '.portfolio-build.html')
OUT = os.path.join(ROOT, 'assets', 'kim-taehun-portfolio.pdf')


def render(html):
    with open(TMP, 'w', encoding='utf-8') as f:
        f.write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    '--virtual-time-budget=15000', f'--print-to-pdf={OUT}', f'file://{TMP}'],
                   stderr=subprocess.DEVNULL, check=True)
    data = open(OUT, 'rb').read()
    kids = [int(x) for x in re.findall(rb'(\d+) 0 R', re.search(rb'/Type\s*/Pages.*?/Kids\s*\[(.*?)\]', data, re.S).group(1))]
    dests = {k.decode(): int(v) for k, v in re.findall(rb'/(nuktu|ege|bustracker) \[(\d+) 0 R', data)}
    return {k: kids.index(v) + 1 for k, v in dests.items()}


src = open(SRC, encoding='utf-8').read()
first = render(src.replace('@P1', '0').replace('@P2', '0').replace('@P3', '0'))
final = src.replace('@P1', str(first['nuktu'])).replace('@P2', str(first['ege'])).replace('@P3', str(first['bustracker']))
second = render(final)
os.remove(TMP)
assert first == second, (first, second)
print('목차 쪽 번호', second)
