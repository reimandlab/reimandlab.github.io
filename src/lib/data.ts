import yaml from 'js-yaml';
import { getCollection, type CollectionEntry } from 'astro:content';
import siteRaw from '../data/site.yaml?raw';
import newsRaw from '../data/news.yaml?raw';

export const site = yaml.load(siteRaw) as any;

// ---------- people & authors ----------
export const roleLabel: Record<string, string> = {
  pi: 'Principal Investigator',
  postdoc: 'Postdoctoral Fellow',
  staff: 'Staff Scientist',
  phd: 'PhD Student',
  msc: 'MSc Student',
  student: 'Research Student',
  visitor: 'Visiting Researcher',
};
const roleOrder = Object.keys(roleLabel);

/** "Jüri Reimand*" -> "reimand j" (surname + first initial, accents removed) */
export function authorKey(name: string): string {
  const t = name.replace(/\*/g, '').normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[.,]/g, ' ').trim().toLowerCase().split(/\s+/);
  return t.length < 2 ? t.join(' ') : `${t[t.length - 1]} ${t[0][0]}`;
}

export async function getPeople() {
  const all = await getCollection('people');
  const sort = (a: CollectionEntry<'people'>, b: CollectionEntry<'people'>) =>
    (roleOrder.indexOf(a.data.role ?? '') - roleOrder.indexOf(b.data.role ?? '')) ||
    (a.data.order - b.data.order) || a.data.name.localeCompare(b.data.name);
  const current = all.filter((p) => p.data.status === 'current').sort(sort);
  const alumni = all.filter((p) => p.data.status === 'alumni')
    .sort((a, b) => a.data.name.split(' ').at(-1)!.localeCompare(b.data.name.split(' ').at(-1)!));
  const labKeys = new Set(all.flatMap((p) => [p.data.name, ...p.data.author_names].map(authorKey)));
  return { current, alumni, labKeys };
}

// ---------- papers ----------
export type Paper = CollectionEntry<'papers'> & { labLed: boolean; href?: string };

export async function getPapers(): Promise<Paper[]> {
  const { labKeys } = await getPeople();
  const papers = await getCollection('papers');
  return papers
    .map((p) => {
      const a = p.data.authors;
      const inferred = labKeys.has(authorKey(a[0])) || labKeys.has(authorKey(a[a.length - 1]));
      const href = p.data.doi ? `https://doi.org/${p.data.doi}` : (p.data.url ?? p.data.preprint);
      return Object.assign(p, { labLed: p.data.lab_led ?? inferred, href });
    })
    .sort((x, y) => y.data.year - x.data.year || x.data.title.localeCompare(y.data.title));
}

// ---------- news ----------
export type NewsItem = { date: Date; type: string; text: string; href?: string };

export async function getNews(): Promise<NewsItem[]> {
  const posts = (await getCollection('posts')).map((p) => ({
    date: p.data.date, type: p.data.type, text: p.data.short, href: `/news/${p.id}/`,
  }));
  const quick = ((yaml.load(newsRaw) as any[]) ?? []).map((n) => ({
    date: new Date(n.date), type: n.type ?? 'update', text: String(n.text), href: n.link,
  }));
  return [...quick, ...posts].sort((a, b) => b.date.getTime() - a.date.getTime());
}

export const fmtMonth = (d: Date) =>
  d.toLocaleDateString('en-CA', { month: 'short', year: 'numeric', timeZone: 'UTC' });
export const fmtDate = (d: Date) =>
  d.toLocaleDateString('en-CA', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });

export const themeLabel: Record<string, string> = {
  drivers: 'Drivers & passengers',
  'multi-omics': 'Multi-omics',
  biomarkers: 'Biomarkers & targets',
};
